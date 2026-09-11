import React, { useState } from 'react';
import { FraudDetector } from './components/FraudDetector';
import { AuditTrailViewer } from './components/AuditTrailViewer';

export default function App() {
  const [data, setData] = useState<any>(null);

  return (
    <div style={{ padding: '2rem', fontFamily: 'system-ui, -apple-system, sans-serif', maxWidth: '900px', margin: '0 auto' }}>
      <header style={{ padding: '1.5rem', background: '#0f172a', color: '#fff', borderRadius: '8px', marginBottom: '1.5rem' }}>
        <h2 style={{ margin: 0 }}>BidMizan Ethical Procurement AI</h2>
        <p style={{ margin: '0.5rem 0 0 0', fontSize: '14px', color: '#94a3b8' }}>
          Monorepo Architecture: FastAPI (`apps/api`) & React 18 TypeScript (`apps/web`)
        </p>
      </header>

      <main style={{ display: 'grid', gap: '1.5rem' }}>
        <FraudDetector onTriage={setData} onScreen={setData} onDiagnose={setData} onCalculate={setData} onExecute={setData} onScan={setData} />
        <AuditTrailViewer triageResult={data} candidate={data} result={data} data={data} trajectory={data} audit={data} />
      </main>
    </div>
  );
}

// Production Live API Integration Ready
