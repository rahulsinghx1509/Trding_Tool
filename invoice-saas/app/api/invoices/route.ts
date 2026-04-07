import { NextRequest, NextResponse } from 'next/server';

import { addInvoice, listInvoices } from '../../../lib/mock-db';
import { InvoiceRecord } from '../../../lib/types';

export async function GET() {
  return NextResponse.json({ data: listInvoices() });
}

export async function POST(request: NextRequest) {
  const body = (await request.json()) as Partial<InvoiceRecord>;

  if (!body.client || !body.customerId || !body.amount || !body.status || !body.dueDate) {
    return NextResponse.json(
      { error: 'client, customerId, amount, status, and dueDate are required' },
      { status: 400 }
    );
  }

  const record: InvoiceRecord = {
    id: body.id || `INV-${Date.now()}`,
    client: body.client,
    customerId: body.customerId,
    amount: body.amount,
    status: body.status,
    dueDate: body.dueDate,
    notes: body.notes || '',
  };

  return NextResponse.json({ data: addInvoice(record) }, { status: 201 });
}
