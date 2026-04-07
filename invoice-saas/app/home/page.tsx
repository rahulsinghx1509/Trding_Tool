import { features, plans } from '../../lib/site-data';

export default function HomePage() {
  return (
    <main>
      <div className="container">
        <nav className="nav">
          <strong>InvoiceFlow</strong>
          <div className="nav-links">
            <a href="/home">Home</a>
            <a href="/features">Features</a>
            <a href="/pricing">Pricing</a>
            <a href="/login">Login</a>
            <a href="/dashboard">Dashboard</a>
          </div>
        </nav>

        <section className="hero">
          <span className="badge">Invoice SaaS starter</span>
          <h1 className="title">Send invoices, track collections, and manage customer billing in one clean workspace.</h1>
          <p className="subtitle">Built for freelancers, agencies, consultants, and small finance teams. Create branded invoices, monitor overdue amounts, and keep your revenue ops tight.</p>
          <div className="actions">
            <a className="btn btn-primary" href="/dashboard">Open dashboard</a>
            <a className="btn btn-secondary" href="/pricing">See pricing</a>
          </div>
        </section>

        <section className="section">
          <div className="grid-2">
            {features.map((feature) => (
              <div className="card" key={feature.title}>
                <h3>{feature.title}</h3>
                <p>{feature.description}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="section">
          <h2>Simple plans that scale with your team</h2>
          <div className="grid-3">
            {plans.map((plan) => (
              <div className="card" key={plan.name}>
                <h3>{plan.name}</h3>
                <div className="title" style={{ fontSize: '38px', marginTop: 8, marginBottom: 8 }}>{plan.price}</div>
                <p>{plan.seats}</p>
                <p>{plan.highlight}</p>
                <a className="btn btn-primary" href="/login">Start free</a>
              </div>
            ))}
          </div>
        </section>
      </div>
    </main>
  );
}
