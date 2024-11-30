import { axiosInstanсe } from './instance';

export const getChats = async () => {
  const response = await axiosInstanсe.get('/chats/');
  return response;
};
