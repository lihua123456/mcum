%% init
map = load('map.txt');

[height, width] = size(map);
start_pos = [];
end_pos = [];
gate_pos = [];
for i = drange(1:height)
    for j = drange(1:width)
        if map(i,j) == 1
            start_pos = [start_pos; [i j]];
        elseif map(i,j) == 2
            end_pos = [end_pos; [i j]];
        elseif map(i,j) == 3
            gate_pos = [gate_pos; [i j]];
        end
    end
end
%% run
car_len = [1,2,3];

car_list = [];
for t = drange(1:600)   % main loop
    if map(start_pos
end