export default function LoginPage() {
  return (
    <main>
      <div className="container" style={{ paddingTop: 48, paddingBottom: 48 }}>
        <nav className="nav">
          <strong>InvoiceFlow</strong>
          <div className="nav-links">
            <a href="/">Home</a>
            <a href="/pricing">Pricing</a>
          </div>
        </nav>
        <div className="card" style={{ maxWidth: 520, margin: '48px auto 0' }}>
          <h1 style={{ marginTop: 0 }}>Welcome back</h1>
          <p className="muted">Secure login screen placeholder for auth integration.</p>
          <div className="actions" style={{ marginTop: 20 }}>
            <a className="btn btn-primary" href="/dashboard">Continue to dashboard</a>
            <a className="btn btn-secondary" href="/pricing">Create workspace</a>
          </div>
        </div>
      </div>
    </main>
  );
}
