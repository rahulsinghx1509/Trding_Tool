import { features } from '../../lib/site-data';

export default function FeaturesPage() {
  return (
    <main>
      <div className="container">
        <nav className="nav">
          <strong>InvoiceFlow</strong>
          <div className="nav-links">
            <a href="/">Home</a>
            <a href="/pricing">Pricing</a>
            <a href="/dashboard">Dashboard</a>
          </div>
        </nav>
        <section className="hero">
          <span className="badge">Features</span>
          <h1 className="title">Everything you need to send invoices and manage collections.</h1>
          <p className="subtitle">Start with the essentials and keep growing into subscriptions, reminders, customer management, analytics, and payment automation.</p>
        </section>
        <section className="section">
          <div className="grid-2">
            {features.map((feature) => (
              <div className="card" key={feature.title}>
                <h3>{feature.title}</h3>
                <p>{feature.description}</p>
              </div>
            ))}
            <div className="card">
              <h3>Automated reminders</h3>
              <p>Schedule reminder emails and follow-ups for unpaid and overdue invoices.</p>
            </div>
            <div className="card">
              <h3>PDF exports</h3>
              <p>Generate branded invoice PDFs with customer details, tax lines, and line items.</p>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}
