 import React, { useState } from 'react';
import axios from 'axios';

function PlainLanguageTranslator() {
  const [text, setText] = useState('');
  const [translation, setTranslation] = useState('');

  const translate = async () => {
    // Call backend endpoint for GPT-4 translation
    const res = await axios.post('http://localhost:5000/api/translate', { text });
    setTranslation(res.data.translation);
  };

  return (
    <div>
      <h2>Plain Language Translator</h2>
      <textarea value={text} onChange={e => setText(e.target.value)} />
      <button onClick={translate}>Translate</button>
      <p>{translation}</p>
    </div>
  );
}

export default PlainLanguageTranslator;
