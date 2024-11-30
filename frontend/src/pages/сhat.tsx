import { Button } from '@mui/material';
import { useQuery } from '@tanstack/react-query';
import { useNavigate } from 'react-router-dom';
import { getChats } from '../api/chats';
import { SkeletonLoader } from '../components';
import { ChatCard } from '../components/chat-card';
import { ChatType } from '../types/chat';

export const Chat = () => {
  const navigate = useNavigate();

  const { data, error, isLoading } = useQuery<ChatType[], Error>({
    queryKey: ['chats'],
    queryFn: getChats,
  });

  const loaders = Array.from({ length: 7 }, (_, index) => <SkeletonLoader key={index} />);

  return (
    <div className="chat-list-container">
      <div className="header">
        <h1>Чаты</h1>
        <Button
          onClick={() => navigate('/login-phone')}
          sx={{ background: 'white', color: '#202b36', marginRight: '60px' }}
          type="submit"
          variant="contained">
          Выйти
        </Button>
      </div>
      <div className="chat-cards">
        {isLoading && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>{loaders}</div>
        )}
        {error && <p>Error: {error.message}</p>}
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
    </div>
  );
};
