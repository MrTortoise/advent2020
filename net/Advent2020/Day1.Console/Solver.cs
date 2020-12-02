using System;
using System.Collections.Generic;
using System.Linq;

namespace Day1.Spec
{
    public class Solver
    {
        public int Solve2(IEnumerable<int> values)
        {
            var valueList = values.ToList();
            for (int outer = 0; outer < valueList.Count; outer++)
            {
                for (int inner = 1; inner < valueList.Count; inner++)
                {
                    var lower = valueList[outer];
                    var upper = valueList[inner];
                    if (lower + upper == 2020)
                    {
                        return lower*upper;
                    }
                }
            }
            throw new ArgumentException("no values add to 2020");
        }

        public int Solve3(IEnumerable<int> values)
        {
            var valueList = values.ToList();
            for (int outer = 0; outer < valueList.Count; outer++)
            {
                for (int inner = 1; inner < valueList.Count; inner++)
                {
                    for (int inner2 = 2; inner2 < valueList.Count; inner2++)
                    {
                        var lower = valueList[outer];
                        var upper = valueList[inner];
                        var upper2 = valueList[inner2];
                        if (lower + upper + upper2 == 2020)
                        {
                            return lower * upper * upper2;
                        }
                    }
                }
            }
            throw new ArgumentException("no values add to 2020");
        }
    }
}