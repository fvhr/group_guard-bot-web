import React from 'react';

type MenuProps = {
  handleRemoveFromChat: () => void;
  handleRemoveFromAllChats: () => void;
};

export const MenuMembers: React.FC<MenuProps> = ({
  handleRemoveFromChat,
  handleRemoveFromAllChats,
}) => {
  return (
    <div className="members__dropdown">
      <button onClick={() => handleRemoveFromChat()}>Удалить из этого чата</button>
      <button onClick={() => handleRemoveFromAllChats()}>Удалить из всех чатов</button>
    </div>
  );
};
