import { ChatCards } from '../components';

export const Chat = () => {
  return (
    <div className="chat-list-container">
      <div className="header">
        <h1>Чаты</h1>
      </div>
      <ChatCards />
    </div>
  );
};
