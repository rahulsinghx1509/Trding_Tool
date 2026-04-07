export default function DashboardPage() {
  return (
    <main>
      <div className="container" style={{ paddingTop: 32, paddingBottom: 48 }}>
        <nav className="nav">
          <strong>InvoiceFlow Dashboard</strong>
          <div className="nav-links">
            <a href="/invoices">Invoices</a>
            <a href="/customers">Customers</a>
            <a href="/">Website</a>
          </div>
        </nav>

        <section className="section">
          <div className="grid-3">
            <div className="kpi"><div className="kpi-label">Revenue</div><div className="kpi-value">₹3.4L</div></div>
            <div className="kpi"><div className="kpi-label">Outstanding</div><div className="kpi-value">₹58K</div></div>
            <div className="kpi"><div className="kpi-label">Clients</div><div className="kpi-value">28</div></div>
          </div>
        </section>

        <section className="section grid-2">
          <div className="card">
            <h2 style={{ marginTop: 0 }}>Recent activity</h2>
            <p>INV-2401 marked paid by Northstar Labs.</p>
            <p>INV-2402 reminder scheduled for tomorrow.</p>
            <p>Monthly cash-flow snapshot updated.</p>
          </div>
          <div className="card">
            <h2 style={{ marginTop: 0 }}>Collection summary</h2>
            <p>Paid this month: ₹2.8L</p>
            <p>Pending collection: ₹58K</p>
            <p>Overdue risk bucket: ₹9.8K</p>
          </div>
        </section>
      </div>
    </main>
  );
}
