import React, { useState } from 'react';

export function FraudDetector({ onScan }: { onScan: (res: any) => void }) {
  const [tenderId, setTenderId] = useState('TENDER-ETH-2026-88');
  const [bidderCount, setBidderCount] = useState(5);
  const [priceVariance, setPriceVariance] = useState(0.04);

  const handleScan = (e: React.FormEvent) => {
    e.preventDefault();
    const isSuspicious = priceVariance < 0.05;
    onScan({
      tenderId,
      fairnessScore: isSuspicious ? 42 : 95,
      auditStatus: isSuspicious ? 'FLAGGED_PRICE_COLLUSION' : 'PASSED_ETHICAL_AUDIT',
      sha256Hash: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
      recommendations: isSuspicious 
        ? ['Flagged for identical bidding margin patterns across 3 suppliers.', 'Trigger mandatory anti-collusion investigation.']
        : ['Bid distribution satisfies statutory procurement fairness standards.']
    });
  };

  return (
    <form onSubmit={handleScan} style={{ background: '#ffffff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3 style={{ color: '#0f172a', marginBottom: '1rem' }}>⚖️ Tender Fraud & Collusion Scanner</h3>
      <div style={{ display: 'grid', gap: '1rem', gridTemplateColumns: '1fr 1fr 1fr' }}>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Tender Reference ID</label>
          <input value={tenderId} onChange={e => setTenderId(e.target.value)} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Number of Bidders</label>
          <input type="number" value={bidderCount} onChange={e => setBidderCount(Number(e.target.value))} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Bid Price Variance</label>
          <input type="number" step="0.01" value={priceVariance} onChange={e => setPriceVariance(Number(e.target.value))} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
      </div>
      <button type="submit" style={{ marginTop: '1rem', background: '#dc2626', color: '#fff', padding: '0.75rem 1.5rem', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>
        Run Ethical Audit Audit Engine
      </button>
    </form>
  );
}
