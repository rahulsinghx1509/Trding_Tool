# Invoice SaaS Database Setup

## Goal

Move the app from mock in-memory data to a real PostgreSQL database using Prisma.

## 1. Install database dependencies

Inside `invoice-saas` run:

```bash
npm install prisma @prisma/client
npx prisma generate
```

## 2. Add database URL

Create `.env.local` inside `invoice-saas` with:

```env
DATABASE_URL="postgresql://USER:PASSWORD@HOST:5432/invoice_saas?schema=public"
```

## 3. Run migration

```bash
npx prisma migrate dev --name init
```

## 4. Test API routes

After setup, these routes should be your next live targets:
- `/api/db/health`
- `/api/db/customers`
- `/api/db/invoices`

## 5. Recommended local database options

- Neon
- Supabase Postgres
- Railway Postgres
- local Postgres via Docker

## 6. Safe rollout order

1. keep current mock routes working
2. configure Prisma and database
3. test DB health route
4. test customers route
5. test invoices route
6. then update frontend pages to consume DB routes
