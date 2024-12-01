import { ChatType } from '../types/chat';
import { Member } from '../types/members';
import { axiosInstanсe } from './instance';

export const getChats = async (): Promise<ChatType[]> => {
  const response = await axiosInstanсe.get<ChatType[]>('/chats/');
  return response.data;
};

export const getCurrentChat = async (id: string): Promise<ChatType> => {
  const response = await axiosInstanсe.get<ChatType>(`chats/${id}/`);
  return response.data;
};

export const getUsersChat = async (id: string): Promise<Member[]> => {
  const response = await axiosInstanсe.get<Member[]>(`chats/${id}/users/`);
  return response.data;
};

export const searchChatMembers = async (id: string, query: string): Promise<Member[]> => {
  const response = await axiosInstanсe.get<Member[]>(`/chats/${id}/users/search`, {
    params: { q: query },
  });
  return response.data;
};
