from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Policy
from ingestion import ingest_policy
from parsing import parse_legalese
from scaledown import scale_down
from impact import assess_impact
import config

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
db.init_app(app)

@app.route('/api/ingest', methods=['POST'])
def ingest():
    url = request.json['url']
    text = ingest_policy(url)
    parsed = parse_legalese(text)
    summary = scale_down(text)
    impact = assess_impact(len(text), len(parsed['stakeholders']))
    policy = Policy(title=request.json.get('title', 'Unknown'), raw_text=text, summary=summary, stakeholders=parsed['stakeholders'], impact_score=impact)
    db.session.add(policy)
    db.session.commit()
    return jsonify({'id': policy.id})

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    # Simple text search; enhance with vector search
    policies = Policy.query.filter(Policy.summary.contains(query)).all()
    return jsonify([{'id': p.id, 'title': p.title, 'summary': p.summary} for p in policies])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 
