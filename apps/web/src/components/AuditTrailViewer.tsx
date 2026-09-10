import React from 'react';

export function AuditTrailViewer({ audit }: { audit: any }) {
  if (!audit) return null;
  const isFlagged = audit.auditStatus.includes('FLAGGED');

  return (
    <div style={{ marginTop: '1.5rem', padding: '1.5rem', background: isFlagged ? '#fef2f2' : '#f0fdf4', border: `1px solid ${isFlagged ? '#fecaca' : '#bbf7d0'}`, borderRadius: '8px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h4 style={{ margin: 0, color: isFlagged ? '#991b1b' : '#166534' }}>
          Fairness Score: {audit.fairnessScore} / 100
        </h4>
        <span style={{ padding: '0.25rem 0.75rem', background: isFlagged ? '#ef4444' : '#22c55e', color: '#fff', borderRadius: '12px', fontSize: '12px', fontWeight: 'bold' }}>
          {audit.auditStatus}
        </span>
      </div>
      <p style={{ marginTop: '0.5rem', fontSize: '12px', color: '#475569', wordBreak: 'break-all' }}>
        <strong>SHA-256 Tamper-Proof Audit Hash:</strong> <code>{audit.sha256Hash}</code>
      </p>
      
      <div style={{ marginTop: '0.75rem', borderTop: '1px solid #e2e8f0', paddingTop: '0.5rem' }}>
        <strong style={{ fontSize: '12px', color: '#334155' }}>Audit Recommendations:</strong>
        <ul style={{ margin: '0.25rem 0 0 1.25rem', color: '#475569', fontSize: '13px' }}>
          {audit.recommendations.map((r: string, idx: number) => (
            <li key={idx}>{r}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
