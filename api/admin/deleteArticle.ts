import type { VercelRequest, VercelResponse } from "@vercel/node";
import { z } from "zod";
import { verifyJWT } from "./login";
import { PrismaClient } from "@prisma/client";
const schema = z.object({
  id: z.string(),
});
export default async function (
  request: VercelRequest,
  response: VercelResponse
) {
  try {
    const { id } = schema.parse(request.body);
    const adminJwt = request.headers.authorization;
    if (!adminJwt) {
      throw new Error("Unauthorized");
    }
    const isVerified = verifyJWT(adminJwt);
    if (!isVerified) {
      throw new Error("Unauthorized");
    }
    const prisma = new PrismaClient();
    const article = await prisma.article.findUnique({
      where: {
        id,
      },
    });
    if (!article) {
      throw new Error("Article not found");
    }
    await prisma.article.delete({
      where: {
        id,
      },
    });
    response.status(200).json({
      ok: true,
    });
  } catch (error) {
    response.status(400).json({ error: error.message });
  }
}
