import React from 'react';

export function AuditLogTable({ records }: { records: any[] }) {
  return (
    <div style={{ background: '#fff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a' }}>📋 Procurement Cryptographic Audit Log</h3>
      {records.length === 0 ? (
        <p style={{ color: '#64748b', fontSize: '14px' }}>No procurement audit records available.</p>
      ) : (
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '14px' }}>
          <thead>
            <tr style={{ background: '#f8fafc', textAlign: 'left', borderBottom: '2px solid #e2e8f0' }}>
              <th style={{ padding: '0.75rem' }}>Tender ID</th>
              <th style={{ padding: '0.75rem' }}>Fairness Score</th>
              <th style={{ padding: '0.75rem' }}>Audit Status</th>
              <th style={{ padding: '0.75rem' }}>SHA-256 Audit Hash</th>
            </tr>
          </thead>
          <tbody>
            {records.map((r, i) => (
              <tr key={i} style={{ borderBottom: '1px solid #e2e8f0' }}>
                <td style={{ padding: '0.75rem', fontWeight: 'bold' }}>{r.tender_id}</td>
                <td style={{ padding: '0.75rem' }}>{r.fairness_score} / 100</td>
                <td style={{ padding: '0.75rem' }}>
                  <span style={{ padding: '0.25rem 0.5rem', borderRadius: '4px', background: r.audit_status.includes('PASSED') ? '#dcfce7' : '#fee2e2', color: r.audit_status.includes('PASSED') ? '#15803d' : '#b91c1c', fontWeight: 'bold', fontSize: '12px' }}>
                    {r.audit_status}
                  </span>
                </td>
                <td style={{ padding: '0.75rem', fontSize: '11px', fontFamily: 'monospace' }}>{r.sha256_hash ? r.sha256_hash.substring(0, 20) + '...' : 'e3b0c44298fc1c14...'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
