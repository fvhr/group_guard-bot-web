export interface IMember {
  id: number;
  name: string;
  avatarUrl: string;
}

export interface IChatListMembersProps {
  chatName: string;
  chatMembersCount: number;
  chatImageUrl: string;
  members: IMember[];
}