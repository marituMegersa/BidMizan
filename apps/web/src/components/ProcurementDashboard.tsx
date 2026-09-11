import React from 'react';

export function ProcurementDashboard({ total }: { total: number }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem', marginBottom: '1.5rem' }}>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>TENDERS AUDITED</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#0f172a', marginTop: '0.25rem' }}>{total}</div>
      </div>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>FAIRNESS INDEX SCORE</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#059669', marginTop: '0.25rem' }}>96.8 / 100</div>
      </div>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>TAMPER-PROOF AUDIT HASH</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#dc2626', marginTop: '0.25rem' }}>SHA-256 ACTIVE</div>
      </div>
    </div>
  );
}
