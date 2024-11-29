import { Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { ChatCard } from '../components/chat-card';

export const Chat = () => {
  const navigate = useNavigate();
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
        <ChatCard
          chatName="ИмяЧатаКрутого"
          description="КрутоеОписаниеЧата"
          imageUrl="https://randomuser.me/api/portraits/men/75.jpg"
        />
        <ChatCard
          chatName="ЕщеБолееКрутоеИмяЧата"
          description="ЕщеБолееКрутоеОписаниеЧата"
          imageUrl="https://randomuser.me/api/portraits/women/45.jpg"
        />
      </div>
    </div>
  );
};
