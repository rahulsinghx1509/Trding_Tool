import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({
    ok: true,
    mode: 'database-starter',
    note: 'Prisma client added. Database-backed CRUD routes to be used after DATABASE_URL and migrations are set.',
  });
}
