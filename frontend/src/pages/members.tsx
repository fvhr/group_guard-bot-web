import { useQuery } from '@tanstack/react-query';
import React from 'react';
import { useParams } from 'react-router-dom';
import { getCurrentChat, getUsersChat } from '../api/chats';
import { ChatListMembers, SkeletonLoader } from '../components/index';
import { ChatType } from '../types/chat';
import { Member } from '../types/members';

export const ChatMembers: React.FC = () => {
  const { id } = useParams<{ id: string }>();

  const {
    data: members,
    error: membersError,
    isLoading: membersLoading,
  } = useQuery<Member[], Error>({
    queryKey: ['users-chat', id],
    queryFn: () => getUsersChat(id!),
    enabled: !!id,
  });

  const {
    data: chatInfo,
    error: chatError,
    isLoading: chatLoading,
  } = useQuery<ChatType, Error>({
    queryKey: ['chat-info', id],
    queryFn: () => getCurrentChat(id!),
    enabled: !!id,
  });

  const isLoading = membersLoading || chatLoading;
  const error = membersError || chatError;

  const loaders = Array.from({ length: 6 }, (_, index) => <SkeletonLoader key={index} />);

  return (
    <div className="members">
      <ChatListMembers
        isLoading={isLoading}
        error={error}
        chatInfo={chatInfo}
        loaders={loaders}
        members={members || []}
      />
    </div>
  );
};
