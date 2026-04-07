import { customers } from '../../lib/site-data';

export default function CustomersPage() {
  return (
    <main>
      <div className="container" style={{ paddingTop: 32, paddingBottom: 48 }}>
        <nav className="nav">
          <strong>InvoiceFlow Customers</strong>
          <div className="nav-links">
            <a href="/dashboard">Dashboard</a>
            <a href="/invoices">Invoices</a>
            <a href="/">Website</a>
          </div>
        </nav>

        <section className="section">
          <div className="grid-3">
            {customers.map((customer) => (
              <div className="card" key={customer.name}>
                <h3>{customer.name}</h3>
                <p>Primary contact: {customer.contact}</p>
                <p>Lifetime spend: {customer.spend}</p>
                <p>Total invoices: {customer.invoices}</p>
              </div>
            ))}
          </div>
        </section>
      </div>
    </main>
  );
}
