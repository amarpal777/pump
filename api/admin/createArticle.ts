import type { VercelRequest, VercelResponse } from "@vercel/node";
import { z } from "zod";
import { verifyJWT } from "./login";
import { PrismaClient } from "@prisma/client";
const schema = z.object({
  title: z.string(),
  content: z.string(),
  img : z.string(),
});
export default async function (
  request: VercelRequest,
  response: VercelResponse
) {
  try {
    const { title, content, img } = schema.parse(request.body);
    const adminJwt = request.headers.authorization;
    if (!adminJwt) {
      throw new Error("Unauthorized");
    }
    const isVerified = verifyJWT(adminJwt);
    if (!isVerified) {
      throw new Error("Unauthorized");
    }

    console.log(title, content);
    const prisma = new PrismaClient();
    await prisma.article.create({
      data: {
        title,
        content,
        imgUrl: img
      },
    });
    return response.send({ ok: true });
  } catch (error) {
    response.send({ ok: false, error: error.message });
  }
}
