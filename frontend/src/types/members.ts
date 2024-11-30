export interface Member {
  user: User;
  is_admin: boolean;
}

type User = {
  id: number;
  username: string;
  first_name: string;
  photo_url: string;
  is_premium: boolean;
};
