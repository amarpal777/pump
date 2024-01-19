import type { VercelRequest, VercelResponse } from "@vercel/node";
import { z } from "zod";
import jsonwebtoken from "jsonwebtoken";
const schema = z.object({
  username: z.string(),
  password: z.string(),
});
export default async function (
  request: VercelRequest,
  response: VercelResponse
) {
  try {
    const { username, password } = schema.parse(request.body);
    const adminPassword = process.env.ADMIN_PASSWORD;
    const adminUsername = "admin";
    if (username !== adminUsername) {
      throw new Error("Invalid username");
    }
    if (password !== adminPassword) {
      throw new Error("Invalid password");
    }
    const adminJwt = jsonwebtoken.sign(
      { username: adminUsername },
      process.env.JWT_KEY!
    );
    return response.send({ ok: true, token: adminJwt });
  } catch (error) {
    response.send({ ok: false, error: error.message });
  }
}

export const verifyJWT = (token: string) => {
  try {
    const decoded = jsonwebtoken.verify(token, process.env.JWT_KEY!);
    return true;
  } catch (error) {
    return false;
  }
};
