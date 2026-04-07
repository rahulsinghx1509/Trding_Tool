export const features = [
  {
    title: 'Faster invoicing',
    description: 'Create polished invoices, recurring billing plans, and branded PDFs in minutes.',
  },
  {
    title: 'Payment tracking',
    description: 'Track paid, partial, overdue, and failed collections from one dashboard.',
  },
  {
    title: 'Client workspace',
    description: 'Store customers, tax rules, billing addresses, and invoice history in one place.',
  },
  {
    title: 'Revenue visibility',
    description: 'Monitor cash flow, overdue amounts, and monthly run-rate with lightweight analytics.',
  },
];

export const plans = [
  { name: 'Starter', price: '₹499', seats: '1 user', highlight: 'Best for freelancers' },
  { name: 'Growth', price: '₹1,499', seats: '5 users', highlight: 'Best for agencies' },
  { name: 'Scale', price: '₹3,499', seats: 'Unlimited', highlight: 'Best for finance teams' },
];

export const invoices = [
  { id: 'INV-2401', client: 'Northstar Labs', amount: '₹18,500', status: 'Paid', dueDate: 'Apr 10' },
  { id: 'INV-2402', client: 'Mango Studio', amount: '₹42,000', status: 'Pending', dueDate: 'Apr 14' },
  { id: 'INV-2403', client: 'Kite People', amount: '₹9,800', status: 'Overdue', dueDate: 'Apr 02' },
];

export const customers = [
  { name: 'Northstar Labs', contact: 'Aman Verma', spend: '₹1.8L', invoices: 12 },
  { name: 'Mango Studio', contact: 'Rhea Shah', spend: '₹96K', invoices: 6 },
  { name: 'Kite People', contact: 'Tarun Jain', spend: '₹42K', invoices: 4 },
];
