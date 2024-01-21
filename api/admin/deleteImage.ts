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
    const adminJwt = request.headers.authorization;
    if (!adminJwt) {
      throw new Error("Unauthorized");
    }
    const isVerified = verifyJWT(adminJwt);
    if (!isVerified) {
      throw new Error("Unauthorized");
    }
    const { id } = schema.parse(request.body);
    const prisma = new PrismaClient();
    const image = await prisma.images.findUnique({
      where: {
        id,
      },
    });
    if (!image) {
      throw new Error("Image not found");
    }
    await prisma.images.delete({
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
