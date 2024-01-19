import type { VercelRequest, VercelResponse } from "@vercel/node";
export default async function (
  request : VercelRequest,
  response : VercelResponse
) {
  response.send("daa");
}
