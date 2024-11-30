import { ChatType } from '../types/chat';
import { User } from '../types/members';
import { axiosInstanсe } from './instance';

export const getChats = async (): Promise<ChatType[]> => {
  const response = await axiosInstanсe.get<ChatType[]>('/chats/');
  return response.data;
};

export const getCurrentChat = async (id: string): Promise<ChatType> => {
  const response = await axiosInstanсe.get<ChatType>(`chats/${id}/`);
  return response.data;
};

export const getUsersChat = async (id: string): Promise<User[]> => {
  const response = await axiosInstanсe.get<User[]>(`chats/${id}/users/`);
  return response.data;
};
