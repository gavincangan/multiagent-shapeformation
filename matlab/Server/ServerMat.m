%This sampmle code is server of multi agents system (MAS) for work on multi
%agents problem .
% Published by Masoud Nadi
% Email : nadimasoud.90@gmail.com
% Copy Write 2015
%% make agents matrix
% This function load agents in random positions in a line
% The sMat matrix is :
% sMat(:,1)=X ; sMat(:,2)=Y ;sMat(:,3)=Z (in 3D environment) ;
% sMat(:,3)=Agent number ( in 2D environment) ; sMat(:,4)=Agent number (in
% 3D environment)

function [ sMat ] = ServerMat( AgentNum,Dim,SizeOfEnvironmet )

    sMat=zeros(AgentNum,Dim);
    for j=1:Dim
        for i=1:AgentNum
            sMat(i,j)=i;
        end
    end
    sMat(:,Dim+1)=(1:AgentNum);
    for i=1:2
        sMat(AgentNum+i,1:Dim)=SizeOfEnvironmet(i,1:Dim);
    end

end
