export type InvoiceStatus = 'Draft' | 'Pending' | 'Paid' | 'Overdue';

export interface CustomerRecord {
  id: string;
  name: string;
  contact: string;
  email: string;
  spend: string;
  invoices: number;
}

export interface InvoiceRecord {
  id: string;
  client: string;
  customerId: string;
  amount: string;
  status: InvoiceStatus;
  dueDate: string;
  notes?: string;
}
