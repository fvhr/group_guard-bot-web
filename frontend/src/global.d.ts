interface Window {
  Telegram: {
    WebApp: {
			onEvent(arg0: string, arg1: (errorData: any) => void): unknown;
      sendData: (data: string) => void;
    };
  };
}