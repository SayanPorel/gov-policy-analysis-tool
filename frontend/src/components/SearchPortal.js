import React, { useState } from 'react';
import axios from 'axios';

function SearchPortal() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const search = async () => {
    const res = await axios.get(`http://localhost:5000/api/search?q=${query}`);
    setResults(res.data);
  };

  return (
    <div>
      <h2>Policy Search Portal</h2>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search policies" />
      <button onClick={search}>Search</button>
      {results.map(r => <div key={r.id}><h3>{r.title}</h3><p>{r.summary}</p></div>)}
    </div>
  );
}

export default SearchPortal; 
