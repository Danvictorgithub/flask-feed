// eslint-disable-next-line @typescript-eslint/no-unused-vars
import NextAuth from "next-auth";

declare module "next-auth" {
  /**
   * Returned by `useSession`, `getSession` and received as a prop on the `SessionProvider` React Context
   */
  interface Session {
    user: {
      id: string;
      username: string;
    };
    access_token: string;
  }
  interface User {
    id: string;
    sub?: string;
    access_token: string;
    username: string;
  }
}
