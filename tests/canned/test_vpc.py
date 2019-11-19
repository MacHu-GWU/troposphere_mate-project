# -*- coding: utf-8 -*-

import pytest
from troposphere_mate.canned import vpc


def test():
    can = vpc.VPCTier(
        PROJECT_NAME="my_project",
        STAGE="dev",
        VPC_CIDR_ID=192,
        N_PUBLIC_SUBNET=2,
        N_PRIVATE_SUBNET=2,
        USE_NAT_GW_PER_PRIVATE_SUBNET_FLAG=True,
    )
    tpl = can.create_template()

    assert can.vpc is not None
    assert can.public_subnet_list is not None
    assert can.private_subnet_list is not None
    assert can.subnet_list is not None
    assert can.igw is not None
    assert can.eip_list is not None
    assert can.ngw_list is not None
    assert can.public_route_table is not None
    assert can.sg_for_ssh_from_anywhere is not None


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
