import { invoices } from '../../lib/site-data';

export default function InvoicesPage() {
  return (
    <main>
      <div className="container" style={{ paddingTop: 32, paddingBottom: 48 }}>
        <nav className="nav">
          <strong>InvoiceFlow Invoices</strong>
          <div className="nav-links">
            <a href="/dashboard">Dashboard</a>
            <a href="/customers">Customers</a>
            <a href="/">Website</a>
          </div>
        </nav>

        <section className="section">
          <div className="grid-3">
            {invoices.map((invoice) => (
              <div className="card" key={invoice.id}>
                <h3>{invoice.id}</h3>
                <p>Client: {invoice.client}</p>
                <p>Amount: {invoice.amount}</p>
                <p>Status: {invoice.status}</p>
                <p>Due date: {invoice.dueDate}</p>
              </div>
            ))}
          </div>
        </section>
      </div>
    </main>
  );
}
