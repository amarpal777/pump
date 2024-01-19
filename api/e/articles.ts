import type { VercelRequest, VercelResponse } from "@vercel/node";
import { PrismaClient } from "@prisma/client";
export default async function (
  request: VercelRequest,
  response: VercelResponse
) {
  const prisma = new PrismaClient();
  return response.send(await prisma.article.findMany());
}
