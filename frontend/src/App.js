import React from 'react';
import SearchPortal from './components/SearchPortal';
import ImpactAnalyzer from './components/ImpactAnalyzer';
import PlainLanguageTranslator from './components/PlainLanguageTranslator';
import CivicEngagementMetrics from './components/CivicEngagementMetrics';

function App() {
  return (
    <div>
      <h1>Government Policy Analysis Tool</h1>
      <SearchPortal />
      <ImpactAnalyzer />
      <PlainLanguageTranslator />
      <CivicEngagementMetrics />
    </div>
  );
}

export default App;
