import NextAuth, { User } from "next-auth";
import Credentials from "next-auth/providers/credentials";

const handler = NextAuth({
  providers: [
    Credentials({
      credentials: {
        username: { label: "username", type: "text" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        const response = await fetch(
          `${process.env.NEXT_PUBLIC_BACKEND_URL}/auth/login`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(credentials),
          },
        );

        if (!response.ok) {
          const error = await response.json();
          throw new Error(error.message || "Authentication failed");
        }

        const res: User = await response.json();
        if (res) {
          return res;
        }
        return null;
      },
    }),
  ],
  session: {
    strategy: "jwt",
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        // This is for newly logged in user
        token.access_token = user.access_token;
        token.username = user.username;
      }
      const res: User = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/auth/me`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token.access_token}`,
          },
        },
      )
        .then((response) => response.json())
        .catch(() => null);
      if (res) {
        token.username = res.username;
        token.email = res.email;
        return token;
      } else {
        throw new Error("Invalid Token");
      }
    },
    async session({ session, token }) {
      session.user.id = token.sub as string;
      session.user.username = token.username as string;
      session.access_token = token.access_token as string;
      return session;
    },
    async redirect({ baseUrl }) {
      return baseUrl;
    },
  },
  pages: {
    error: "/auth/sign_in?",
    signIn: "/auth/sign_in",
  },
});

export { handler as GET, handler as POST };
