function unpackCommandsJSONandUpdateCommandView(data) {
    let commands = data['commands'];
    let time = '';
    if (commands.length > 0) {$('#commands-count').text(`(${commands.length} total)`)}
    for (i in commands) {
      
      if (commands[i]['time'] != '0') {time = `(${parseFloat(commands[i]['time']).toFixed(2)} ms)`;} 
      else {time = '';}

      $('.redis-commands-output').append(`<li class="redis-command">> ${commands[i]['command']} ${time}</li>`);
    }
    return data['last_id'];
  }

function populateRedisCommands(guid) {return $.getJSON(`/api/communicator/${guid}`, unpackCommandsJSONandUpdateCommandView);}
function updateRedisCommands(guid, lastId) {return $.getJSON(`/api/communicator/${guid}?start_at=${lastId}`, unpackCommandsJSONandUpdateCommandView)}

function pollRedisCommands(guid, promise, pollInterval) {
  
    Promise.resolve(promise).then((data) => {
    var newPromise = updateRedisCommands(guid, data['last_id']);
    setTimeout(() => {
      pollRedisCommands(guid, newPromise, pollInterval);
    }, pollInterval);
  })
}