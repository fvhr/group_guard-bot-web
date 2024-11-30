import { useQuery } from '@tanstack/react-query';
import { getChats } from '../api/chats';
import { ChatCard } from '../components/chat-card';
import { ChatType } from '../types/chat';
import { SkeletonLoader } from './skeleton';

export const ChatCards = () => {
  const { data, error, isLoading } = useQuery<ChatType[], Error>({
    queryKey: ['chats'],
    queryFn: getChats,
  });

  const loaders = Array.from({ length: 7 }, (_, index) => <SkeletonLoader key={index} />);
  return (
    <div className="chat-cards">
      {isLoading && <div className="chat-cards__loading">{loaders}</div>}
      {error && <p className="chat-cards__error">Error: {error.message}</p>}
      {data?.map((el) => (
        <ChatCard
          key={el.id}
          id={el.id}
          chatName={el.title}
          description={el.description}
          imageUrl={el.avatar_url}
        />
      ))}
    </div>
  );
};
