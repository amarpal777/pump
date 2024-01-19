import type { VercelRequest, VercelResponse } from "@vercel/node";
import { PrismaClient } from "@prisma/client";
export default async function (
  request: VercelRequest,
  response: VercelResponse
) {
  const prisma = new PrismaClient();
  const { id } = request.query as { id: string };
  try {
    if (id) {
      const single = await prisma.article.findUnique({
        where: {
          id,
        },
      });
      response.status(200).json(single);
    } else {
      response.status(400).json({ error: "id is required" });
    }
  } catch (error: any) {
    return response.status(500).json({ error:"Something went wrong" });
  }
}
