import './globals.css';

export const metadata = {
  title: 'InvoiceFlow',
  description: 'Invoice SaaS for freelancers and teams',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
