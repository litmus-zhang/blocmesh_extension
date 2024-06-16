chrome.storage.local.set({ message: "Hello World!" }, () => {
    console.log('Value stored in chrome.storage');
});
