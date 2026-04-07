import { plans } from '../../lib/site-data';

export default function PricingPage() {
  return (
    <main>
      <div className="container">
        <nav className="nav">
          <strong>InvoiceFlow</strong>
          <div className="nav-links">
            <a href="/">Home</a>
            <a href="/features">Features</a>
            <a href="/login">Login</a>
          </div>
        </nav>
        <section className="hero">
          <span className="badge">Pricing</span>
          <h1 className="title">Simple pricing for solo operators and growing finance teams.</h1>
          <p className="subtitle">Start small, then unlock team permissions, branded documents, automations, and premium support when you need them.</p>
        </section>
        <section className="section">
          <div className="grid-3">
            {plans.map((plan) => (
              <div className="card" key={plan.name}>
                <h3>{plan.name}</h3>
                <div className="title" style={{ fontSize: '42px', marginTop: 8, marginBottom: 8 }}>{plan.price}</div>
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
