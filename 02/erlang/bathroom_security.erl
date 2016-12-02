-module(bathroom_security).

%% API
-export([part1/0, part2/0]).

part1() ->
  readlines("input").

%% 1 2 3
%% 4 5 6
%% 7 8 9
findcode(Key, []) -> Key;
findcode($1, [$D|Inst]) -> findcode($4, Inst);
findcode($1, [$R|Inst]) -> findcode($2, Inst);
findcode($2, [$D|Inst]) -> findcode($5, Inst);
findcode($2, [$L|Inst]) -> findcode($1, Inst);
findcode($2, [$R|Inst]) -> findcode($3, Inst);
findcode($3, [$D|Inst]) -> findcode($6, Inst);
findcode($3, [$L|Inst]) -> findcode($2, Inst);
findcode($4, [$U|Inst]) -> findcode($1, Inst);
findcode($4, [$D|Inst]) -> findcode($7, Inst);
findcode($4, [$R|Inst]) -> findcode($5, Inst);
findcode($5, [$U|Inst]) -> findcode($2, Inst);
findcode($5, [$D|Inst]) -> findcode($8, Inst);
findcode($5, [$L|Inst]) -> findcode($4, Inst);
findcode($5, [$R|Inst]) -> findcode($6, Inst);
findcode($6, [$U|Inst]) -> findcode($3, Inst);
findcode($6, [$D|Inst]) -> findcode($9, Inst);
findcode($6, [$L|Inst]) -> findcode($5, Inst);
findcode($7, [$U|Inst]) -> findcode($4, Inst);
findcode($7, [$R|Inst]) -> findcode($8, Inst);
findcode($8, [$U|Inst]) -> findcode($5, Inst);
findcode($8, [$L|Inst]) -> findcode($7, Inst);
findcode($8, [$R|Inst]) -> findcode($9, Inst);
findcode($9, [$U|Inst]) -> findcode($6, Inst);
findcode($9, [$L|Inst]) -> findcode($8, Inst);
findcode(K, [_|Inst]) -> findcode(K, Inst).

readlines(FileName) ->
  {ok, Fd} = file:open(FileName, [read]),
  Lines = get_lines(Fd, []),
  process_lines($5, Lines, []).

get_lines(Fd, Acc) ->
  case io:get_line(Fd, "") of
    eof -> file:close(Fd), Acc;
    Line -> get_lines(Fd, lists:append(Acc, [Line]))
  end.

process_lines(Key, [H|[]], Code) ->
  lists:append(Code, [findcode(Key, H)]);
process_lines(Key, [H|T], Code) ->
  NewKey = findcode(Key, H),
  process_lines(NewKey, T, lists:append(Code, [NewKey])).

part2() ->
  readlines2("input").

%%     1
%%   2 3 4
%% 5 6 7 8 9
%%   A B C
%%     D
findcode2(Key, []) -> Key;
findcode2($1, [$D|Inst]) -> findcode2($3, Inst);
findcode2($2, [$D|Inst]) -> findcode2($6, Inst);
findcode2($2, [$R|Inst]) -> findcode2($3, Inst);
findcode2($3, [$U|Inst]) -> findcode2($1, Inst);
findcode2($3, [$D|Inst]) -> findcode2($7, Inst);
findcode2($3, [$L|Inst]) -> findcode2($2, Inst);
findcode2($3, [$R|Inst]) -> findcode2($4, Inst);
findcode2($4, [$D|Inst]) -> findcode2($8, Inst);
findcode2($4, [$L|Inst]) -> findcode2($3, Inst);
findcode2($5, [$R|Inst]) -> findcode2($6, Inst);
findcode2($6, [$U|Inst]) -> findcode2($2, Inst);
findcode2($6, [$D|Inst]) -> findcode2($A, Inst);
findcode2($6, [$L|Inst]) -> findcode2($5, Inst);
findcode2($6, [$R|Inst]) -> findcode2($7, Inst);
findcode2($7, [$U|Inst]) -> findcode2($3, Inst);
findcode2($7, [$D|Inst]) -> findcode2($B, Inst);
findcode2($7, [$L|Inst]) -> findcode2($6, Inst);
findcode2($7, [$R|Inst]) -> findcode2($8, Inst);
findcode2($8, [$U|Inst]) -> findcode2($4, Inst);
findcode2($8, [$D|Inst]) -> findcode2($C, Inst);
findcode2($8, [$L|Inst]) -> findcode2($7, Inst);
findcode2($8, [$R|Inst]) -> findcode2($9, Inst);
findcode2($9, [$L|Inst]) -> findcode2($8, Inst);
findcode2($A, [$U|Inst]) -> findcode2($6, Inst);
findcode2($A, [$R|Inst]) -> findcode2($B, Inst);
findcode2($B, [$U|Inst]) -> findcode2($7, Inst);
findcode2($B, [$D|Inst]) -> findcode2($D, Inst);
findcode2($B, [$L|Inst]) -> findcode2($A, Inst);
findcode2($B, [$R|Inst]) -> findcode2($C, Inst);
findcode2($C, [$U|Inst]) -> findcode2($8, Inst);
findcode2($C, [$L|Inst]) -> findcode2($B, Inst);
findcode2($D, [$U|Inst]) -> findcode2($B, Inst);
findcode2(K, [_|Inst]) -> findcode2(K, Inst).

readlines2(FileName) ->
  {ok, Fd} = file:open(FileName, [read]),
  Lines = get_lines2(Fd, []),
  process_lines2($5, Lines, []).

get_lines2(Fd, Acc) ->
  case io:get_line(Fd, "") of
    eof -> file:close(Fd), Acc;
    Line -> get_lines2(Fd, lists:append(Acc, [Line]))
  end.

process_lines2(Key, [H|[]], Code) ->
  lists:append(Code, [findcode2(Key, H)]);
process_lines2(Key, [H|T], Code) ->
  NewKey = findcode2(Key, H),
  process_lines2(NewKey, T, lists:append(Code, [NewKey])).
