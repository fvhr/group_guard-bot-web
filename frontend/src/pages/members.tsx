import { useQuery } from '@tanstack/react-query';
import { debounce } from 'lodash';
import React, { useCallback, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getCurrentChat, getUsersChat, searchChatMembers } from '../api/chats';
import { ChatListMembers, SkeletonLoader } from '../components/index';
import { ChatType } from '../types/chat';
import { Member } from '../types/members';

export const ChatMembers: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [debouncedQuery, setDebouncedQuery] = useState<string>('');
  const [countNumber, setCountNumber] = useState(0);
	const [isCountSet, setIsCountSet] = useState<boolean>(false); 

  const debouncedSearch = useCallback(
    debounce((query: string) => {
      setDebouncedQuery(query);
    }, 500),
    [],
  );

  const handleSearchChange = (query: string) => {
    setSearchQuery(query);
    debouncedSearch(query);
  };

  const {
    data: members = [],
    error: membersError,
    isLoading: membersLoading,
  } = useQuery<Member[], Error>({
    queryKey: ['users-chat', id, debouncedQuery],
    queryFn: () => (debouncedQuery ? searchChatMembers(id!, debouncedQuery) : getUsersChat(id!)),
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
    refetchOnWindowFocus: false,
  });

  useEffect(() => {
    if (!membersLoading && !isCountSet) {
      setCountNumber(members.length);
      setIsCountSet(true); 
    }
  }, [membersLoading, members.length, isCountSet]);

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
        members={members}
        onSearch={handleSearchChange}
        searchQuery={searchQuery}
        countMembers={countNumber}
      />
    </div>
  );
};
