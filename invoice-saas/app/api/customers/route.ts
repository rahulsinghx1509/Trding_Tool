import { NextRequest, NextResponse } from 'next/server';

import { addCustomer, listCustomers } from '../../../lib/mock-db';
import { CustomerRecord } from '../../../lib/types';

export async function GET() {
  return NextResponse.json({ data: listCustomers() });
}

export async function POST(request: NextRequest) {
  const body = (await request.json()) as Partial<CustomerRecord>;

  if (!body.name || !body.contact || !body.email) {
    return NextResponse.json(
      { error: 'name, contact, and email are required' },
      { status: 400 }
    );
  }

  const record: CustomerRecord = {
    id: body.id || `cus_${Date.now()}`,
    name: body.name,
    contact: body.contact,
    email: body.email,
    spend: body.spend || '₹0',
    invoices: body.invoices || 0,
  };

  return NextResponse.json({ data: addCustomer(record) }, { status: 201 });
}
