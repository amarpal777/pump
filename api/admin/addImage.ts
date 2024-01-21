import type { VercelRequest, VercelResponse } from "@vercel/node";
import { z } from "zod";
import { verifyJWT } from "./login";
import { PrismaClient } from "@prisma/client";
const schema = z.object({
  url: z.string(),
});
export default async function (
  request: VercelRequest,
  response: VercelResponse
) {
  try {
    const adminJwt = request.headers.authorization;
    if (!adminJwt) {
      throw new Error("Unauthorized");
    }
    const isVerified = verifyJWT(adminJwt);
    if (!isVerified) {
      throw new Error("Unauthorized");
    }
    const { url } = schema.parse(request.body);
    const prisma = new PrismaClient();
    await prisma.images.create({
      data: {
        url,
      },
    });
    return response.status(200).json({
      ok: true,
    });
  } catch (error) {
    return response.status(400).json({ error: error.message });
  }
  
}
