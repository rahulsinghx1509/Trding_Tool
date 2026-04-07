import { NextResponse } from 'next/server';

import { findInvoice } from '../../../../lib/mock-db';

export async function GET(
  _request: Request,
  { params }: { params: { id: string } }
) {
  const invoice = findInvoice(params.id);

  if (!invoice) {
    return NextResponse.json({ error: 'Invoice not found' }, { status: 404 });
  }

  return NextResponse.json({ data: invoice });
}
