import { CustomerRecord, InvoiceRecord } from './types';

let customers: CustomerRecord[] = [
  {
    id: 'cus_001',
    name: 'Northstar Labs',
    contact: 'Aman Verma',
    email: 'aman@northstar.test',
    spend: '₹1.8L',
    invoices: 12,
  },
  {
    id: 'cus_002',
    name: 'Mango Studio',
    contact: 'Rhea Shah',
    email: 'rhea@mangostudio.test',
    spend: '₹96K',
    invoices: 6,
  },
];

let invoices: InvoiceRecord[] = [
  {
    id: 'INV-2401',
    client: 'Northstar Labs',
    customerId: 'cus_001',
    amount: '₹18,500',
    status: 'Paid',
    dueDate: '2026-04-10',
    notes: 'Paid via bank transfer',
  },
  {
    id: 'INV-2402',
    client: 'Mango Studio',
    customerId: 'cus_002',
    amount: '₹42,000',
    status: 'Pending',
    dueDate: '2026-04-14',
    notes: 'Reminder scheduled',
  },
];

export function listCustomers(): CustomerRecord[] {
  return customers;
}

export function addCustomer(record: CustomerRecord): CustomerRecord {
  customers = [record, ...customers];
  return record;
}

export function listInvoices(): InvoiceRecord[] {
  return invoices;
}

export function addInvoice(record: InvoiceRecord): InvoiceRecord {
  invoices = [record, ...invoices];
  return record;
}

export function findInvoice(id: string): InvoiceRecord | undefined {
  return invoices.find((invoice) => invoice.id === id);
}
